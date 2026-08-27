import { useState } from "react";
import { Link } from "react-router-dom";

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

        <Link to="/" className="navbar-brand" onClick={closeMenu}>
          <img src={voteraLogo} alt="Votera" />
        </Link>

        <nav
          className={`navbar-links ${
            menuOpen ? "navbar-links-open" : ""
          }`}
        >

          <Link to="/" onClick={closeMenu}>
            Home
          </Link>

          <Link to="/elections" onClick={closeMenu}>
            Elections
          </Link>

          <Link to="/#how-it-works" onClick={closeMenu}>
            How It Works
          </Link>

          <Link to="/#about" onClick={closeMenu}>
            About
          </Link>

          <Link
            to="/elections"
            className="navbar-action"
            onClick={closeMenu}
          >
            Find an Election
          </Link>

        </nav>

        <button
          type="button"
          className={`navbar-toggle ${
            menuOpen ? "navbar-toggle-active" : ""
          }`}
          onClick={() => setMenuOpen(!menuOpen)}
          aria-label={
            menuOpen
              ? "Close navigation menu"
              : "Open navigation menu"
          }
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