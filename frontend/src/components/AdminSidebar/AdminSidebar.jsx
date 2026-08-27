import { NavLink } from "react-router-dom";
import "./AdminSidebar.css";

function AdminSidebar({ electionId }) {
  const navigationItems = [
    {
      label: "Overview",
      path: `/admin/election/${electionId}`,
      icon: "⌂",
    },
    {
      label: "Election",
      path: `/admin/election/${electionId}/election`,
      icon: "◈",
    },
    {
      label: "Positions",
      path: `/admin/election/${electionId}/positions`,
      icon: "☷",
    },
    {
      label: "Candidates",
      path: `/admin/election/${electionId}/candidates`,
      icon: "♙",
    },
    {
      label: "Voters",
      path: `/admin/election/${electionId}/voters`,
      icon: "♧",
    },
    {
      label: "Transactions",
      path: `/admin/election/${electionId}/transactions`,
      icon: "▣",
    },
    {
      label: "Results",
      path: `/admin/election/${electionId}/results`,
      icon: "♛",
    },
  ];

  return (
    <aside className="admin-sidebar">
      <div className="admin-sidebar-brand">
        <div className="admin-sidebar-logo">
          V
        </div>

        <div>
          <h2>Votera</h2>
          <span>Election Admin</span>
        </div>
      </div>

      <nav className="admin-sidebar-nav">
        <span className="admin-nav-label">
          MANAGEMENT
        </span>

        {navigationItems.map((item) => (
          <NavLink
            key={item.label}
            to={item.path}
            end={item.label === "Overview"}
            className={({ isActive }) =>
              isActive
                ? "admin-nav-link active"
                : "admin-nav-link"
            }
          >
            <span className="admin-nav-icon">
              {item.icon}
            </span>

            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>

      <div className="admin-sidebar-bottom">
        <NavLink
          to={`/admin/election/${electionId}/settings`}
          className={({ isActive }) =>
            isActive
              ? "admin-nav-link active"
              : "admin-nav-link"
          }
        >
          <span className="admin-nav-icon">⚙</span>
          <span>Settings</span>
        </NavLink>

        <button
          type="button"
          className="admin-logout-button"
        >
          <span className="admin-nav-icon">↪</span>
          <span>Logout</span>
        </button>
      </div>
    </aside>
  );
}

export default AdminSidebar;