let token = "";

function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `username=${email}&password=${password}`,
  })
    .then(res => res.json())
    .then(data => {
      token = data.access_token;
      alert("Login berhasil!");
    })
    .catch(err => alert("Login gagal"));
}

function getUsers() {
  fetch("/admin/users", {
    headers: { Authorization: `Bearer ${token}` },
  })
    .then(res => res.json())
    .then(users => {
      const tbody = document.querySelector("#userTable tbody");
      tbody.innerHTML = "";
      users.forEach(u => {
        tbody.innerHTML += `
          <tr>
            <td>${u.id}</td>
            <td>${u.email}</td>
            <td>${u.role}</td>
            <td><button class="btn btn-danger btn-sm" onclick="deleteUser(${u.id})">Delete</button></td>
          </tr>`;
      });
    });
}

function deleteUser(id) {
  fetch(`/admin/users/${id}`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` },
  })
    .then(() => {
      alert("User deleted");
      getUsers();
    });
}
