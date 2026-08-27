import { Outlet, useParams } from "react-router-dom";

import AdminSidebar from "../AdminSidebar/AdminSidebar";

import "./AdminLayout.css";

function AdminLayout() {
  const { electionId } = useParams();

  return (
    <div className="admin-layout">

      <AdminSidebar electionId={electionId} />

      <main className="admin-main">
        <Outlet />
      </main>

    </div>
  );
}

export default AdminLayout;