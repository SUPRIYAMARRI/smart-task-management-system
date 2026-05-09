from flask import Blueprint, jsonify
from flask_login import login_required, current_user
import pandas as pd
import numpy as np
from app.models import Task

analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/summary", methods=["GET"])
@login_required
def summary():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    rows = [t.to_dict() for t in tasks]

    if not rows:
        return jsonify({
            "total": 0,
            "completed": 0,
            "pending": 0,
            "in_progress": 0,
            "completion_percentage": 0.0,
            "by_priority": {},
        })

    df = pd.DataFrame(rows)

    total = int(len(df))
    status_counts = df["status"].value_counts().to_dict()
    completed = int(status_counts.get("Completed", 0))
    pending = int(status_counts.get("Pending", 0))
    in_progress = int(status_counts.get("In Progress", 0))

    # NumPy: completion percentage with safe divide
    completion_pct = float(np.round(np.divide(completed, total) * 100, 2)) if total else 0.0

    by_priority = df["priority"].value_counts().to_dict()
    by_priority = {k: int(v) for k, v in by_priority.items()}

    return jsonify({
        "total": total,
        "completed": completed,
        "pending": pending,
        "in_progress": in_progress,
        "completion_percentage": completion_pct,
        "by_priority": by_priority,
    })
