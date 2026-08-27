import { useState } from "react";
import voteraLogo from "../../assets/votera-logo.png";
import "./Navbar.css";

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  const closeMenu = () => {
    setMenuOpen(false);
  };

  return (
    <header className="navbar">
      <div className="navbar-shell">
        <a href="#home" className="navbar-brand" onClick={closeMenu}>
          <img src={voteraLogo} alt="Votera" />
        </a>

        <nav className={`navbar-links ${menuOpen ? "navbar-links-open" : ""}`}>
          <a href="#home" onClick={closeMenu}>
            Home
          </a>

          <a href="elections" onClick={closeMenu}>
            Elections
          </a>

          <a href="#how-it-works" onClick={closeMenu}>
            How It Works
          </a>

          <a href="#about" onClick={closeMenu}>
            About
          </a>

          <a
            href="#elections"
            className="navbar-action"
            onClick={closeMenu}
          >
            Find an Election
          </a>
        </nav>

        <button
          type="button"
          className={`navbar-toggle ${menuOpen ? "navbar-toggle-active" : ""}`}
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label={menuOpen ? "Close navigation menu" : "Open navigation menu"}
          aria-expanded={menuOpen}
        >
          <span />
          <span />
          <span />
        </button>
      </div>
    </header>
  );
}

export default Navbar;