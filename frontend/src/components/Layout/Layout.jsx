import { Outlet } from "react-router-dom";
import Navbar from "../Navbar/Navbar";
import Footer from "../Footer/Footer";
import "./Layout.css";

function Layout() {
  return (
    <div className="app-layout">
      <Navbar />

      <main className="app-content">
        <Outlet />
      </main>

      <Footer />
    </div>
  );
}

export default Layout;