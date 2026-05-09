from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Task
from app.sockets import broadcast_task_event

tasks_bp = Blueprint("tasks", __name__)

VALID_PRIORITY = {"Low", "Medium", "High"}
VALID_STATUS = {"Pending", "In Progress", "Completed"}


@tasks_bp.route("", methods=["GET"])
@login_required
def list_tasks():
    tasks = (
        Task.query.filter_by(user_id=current_user.id)
        .order_by(Task.created_date.desc())
        .all()
    )
    return jsonify([t.to_dict() for t in tasks])


@tasks_bp.route("", methods=["POST"])
@login_required
def create_task():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "Title is required"}), 400

    priority = data.get("priority", "Medium")
    status = data.get("status", "Pending")
    if priority not in VALID_PRIORITY or status not in VALID_STATUS:
        return jsonify({"error": "Invalid priority or status"}), 400

    task = Task(
        user_id=current_user.id,
        title=title,
        description=data.get("description", ""),
        priority=priority,
        status=status,
    )
    db.session.add(task)
    db.session.commit()

    payload = task.to_dict()
    broadcast_task_event("task_created", payload)
    return jsonify(payload), 201


@tasks_bp.route("/<int:task_id>", methods=["PUT", "PATCH"])
@login_required
def update_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json(silent=True) or {}
    if "title" in data:
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify({"error": "Title cannot be empty"}), 400
        task.title = title
    if "description" in data:
        task.description = data["description"]
    if "priority" in data:
        if data["priority"] not in VALID_PRIORITY:
            return jsonify({"error": "Invalid priority"}), 400
        task.priority = data["priority"]
    if "status" in data:
        if data["status"] not in VALID_STATUS:
            return jsonify({"error": "Invalid status"}), 400
        task.status = data["status"]

    db.session.commit()
    payload = task.to_dict()
    broadcast_task_event("task_updated", payload)
    return jsonify(payload)


@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    broadcast_task_event("task_deleted", {"id": task_id})
    return jsonify({"success": True})
