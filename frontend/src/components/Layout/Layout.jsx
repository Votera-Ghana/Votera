import Navbar from "../Navbar/Navbar";
import Footer from "../Footer/Footer";
import "./Layout.css";

function Layout({ children }) {
  return (
    <div className="app-layout">
      <Navbar />

      <main className="app-content">
        {children}
      </main>

      <Footer />
    </div>
  );
}

export default Layout;