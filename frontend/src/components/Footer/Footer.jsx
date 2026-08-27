import { Link, useNavigate } from "react-router-dom";

import "./Footer.css";

import logo from "../../assets/votera-logo.png";

function Footer() {
  const navigate = useNavigate();

  const handleSectionNavigation = (sectionId) => {
    navigate(`/#${sectionId}`);

    setTimeout(() => {
      const section = document.getElementById(sectionId);

      if (section) {
        section.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    }, 100);
  };

  return (
    <footer className="footer">
      <div className="footer-container">

        {/* Brand */}
        <div className="footer-main">

          <div className="footer-brand">
            <Link to="/" className="footer-logo-link">
              <img
                src={logo}
                alt="Votera"
                className="footer-logo"
              />
            </Link>

            <p>
              Simple, secure, and transparent digital voting
              for organizations and communities.
            </p>
          </div>

          {/* Links */}
          <div className="footer-links">

            {/* Platform */}
            <div className="footer-column">
              <h4>Platform</h4>

              <Link to="/">
                Home
              </Link>

              <Link to="/elections">
                Elections
              </Link>

              <button
                type="button"
                onClick={() =>
                  handleSectionNavigation("how-it-works")
                }
              >
                How It Works
              </button>
            </div>

            {/* Company */}
            <div className="footer-column">
              <h4>Company</h4>

              <button
                type="button"
                onClick={() =>
                  handleSectionNavigation("about")
                }
              >
                About
              </button>

              <button
                type="button"
                onClick={() =>
                  handleSectionNavigation("contact")
                }
              >
                Contact
              </button>
            </div>

            {/* Get Started */}
            <div className="footer-column">
              <h4>Get Started</h4>

              <Link to="/elections">
                Find an Election
              </Link>

              <button
                type="button"
                onClick={() =>
                  handleSectionNavigation("how-it-works")
                }
              >
                How Voting Works
              </button>
            </div>

          </div>
        </div>

        {/* Bottom */}
        <div className="footer-bottom">
          <span>
            © 2026 Votera. All rights reserved.
          </span>

          <span className="footer-tagline">
            Your Voice. Your Choice.
          </span>
        </div>

      </div>
    </footer>
  );
}

export default Footer;