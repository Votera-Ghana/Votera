import "./Footer.css";
import logo from "../../assets/votera-logo.png";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">

        <div className="footer-main">
          <div className="footer-brand">
            <img
              src={logo}
              alt="Votera"
              className="footer-logo"
            />

            <p>
              Simple, secure, and transparent digital voting
              for organizations and communities.
            </p>
          </div>

          <div className="footer-links">
            <div className="footer-column">
              <h4>Platform</h4>

              <a href="#home">Home</a>
              <a href="#elections">Elections</a>
              <a href="#how-it-works">How It Works</a>
            </div>

            <div className="footer-column">
              <h4>Company</h4>

              <a href="#about">About</a>
              <a href="#contact">Contact</a>
            </div>

            <div className="footer-column">
              <h4>Get Started</h4>

              <a href="#elections">Find an Election</a>
              <a href="#how-it-works">How Voting Works</a>
            </div>
          </div>
        </div>

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