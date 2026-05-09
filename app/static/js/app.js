// Smart Tasks dashboard logic
const API = "/api/tasks";
const ANALYTICS = "/api/analytics/summary";

const taskList = document.getElementById("task-list");
const form = document.getElementById("task-form");
const liveIndicator = document.getElementById("live-indicator");

const socket = io();

socket.on("connect", () => liveIndicator.classList.remove("disconnected"));
socket.on("disconnect", () => liveIndicator.classList.add("disconnected"));
socket.on("task_created", () => { loadTasks(); loadAnalytics(); });
socket.on("task_updated", () => { loadTasks(); loadAnalytics(); });
socket.on("task_deleted", () => { loadTasks(); loadAnalytics(); });

async function loadTasks() {
  const res = await fetch(API);
  if (!res.ok) return;
  const tasks = await res.json();
  renderTasks(tasks);
}

function renderTasks(tasks) {
  taskList.innerHTML = "";
  if (!tasks.length) {
    taskList.innerHTML = `<li class="muted small">No tasks yet — add one above.</li>`;
    return;
  }
  for (const t of tasks) {
    const li = document.createElement("li");
    li.className = "task";
    li.innerHTML = `
      <div class="task-main">
        <p class="task-title">${escapeHtml(t.title)}</p>
        ${t.description ? `<p class="task-desc">${escapeHtml(t.description)}</p>` : ""}
        <div class="task-meta">
          <span class="badge priority-${t.priority}">${t.priority}</span>
          <span class="badge status-${t.status.replace(" ", ".")}">${t.status}</span>
          <span class="muted small">${new Date(t.created_date).toLocaleString()}</span>
        </div>
      </div>
      <div class="actions">
        <select data-id="${t.id}" class="status-select btn-sm">
          ${["Pending","In Progress","Completed"].map(s =>
            `<option ${s===t.status?"selected":""}>${s}</option>`).join("")}
        </select>
        <button data-id="${t.id}" class="btn btn-sm btn-danger delete-btn">Delete</button>
      </div>`;
    taskList.appendChild(li);
  }

  taskList.querySelectorAll(".delete-btn").forEach(b =>
    b.addEventListener("click", () => deleteTask(b.dataset.id)));
  taskList.querySelectorAll(".status-select").forEach(s =>
    s.addEventListener("change", e => updateStatus(s.dataset.id, e.target.value)));
}

async function loadAnalytics() {
  const res = await fetch(ANALYTICS);
  if (!res.ok) return;
  const a = await res.json();
  document.getElementById("stat-total").textContent = a.total;
  document.getElementById("stat-completed").textContent = a.completed;
  document.getElementById("stat-pending").textContent = a.pending;
  document.getElementById("stat-pct").textContent = a.completion_percentage + "%";
  document.getElementById("progress-bar").style.width = a.completion_percentage + "%";
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const body = {
    title: document.getElementById("title").value,
    description: document.getElementById("description").value,
    priority: document.getElementById("priority").value,
    status: document.getElementById("status").value,
  };
  const res = await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (res.ok) form.reset();
});

async function deleteTask(id) {
  if (!confirm("Delete this task?")) return;
  await fetch(`${API}/${id}`, { method: "DELETE" });
}

async function updateStatus(id, status) {
  await fetch(`${API}/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status }),
  });
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({
    "&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"
  }[c]));
}

loadTasks();
loadAnalytics();
