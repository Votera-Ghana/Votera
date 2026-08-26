import "./Hero.css";

function Hero() {
  return (
    <section className="hero" id="home">
      <div className="hero-container">
        <div className="hero-content">
          <span className="hero-eyebrow">
            Modern Digital Voting
          </span>

          <h1>
            Your Voice.
            <span>Your Choice.</span>
          </h1>

          <p className="hero-description">
            Simple, secure, and transparent digital voting for
            organizations, universities, schools, clubs, and
            associations.
          </p>

          <div className="hero-actions">
            <a href="#elections" className="hero-primary-button">
              Find an Election
            </a>

            <a href="#how-it-works" className="hero-secondary-button">
              How It Works
            </a>
          </div>

          <div className="hero-trust">
            <div className="hero-trust-item">
              <span className="hero-trust-dot" />
              <span>Secure voting</span>
            </div>

            <div className="hero-trust-item">
              <span className="hero-trust-dot" />
              <span>Transparent results</span>
            </div>

            <div className="hero-trust-item">
              <span className="hero-trust-dot" />
              <span>Easy to use</span>
            </div>
          </div>
        </div>

        <div className="hero-visual" aria-hidden="true">
          <div className="hero-glow" />

          <div className="hero-card">
            <div className="hero-card-header">
              <div>
                <span className="hero-card-label">
                  ACTIVE ELECTION
                </span>

                <h2>Student Leadership Election</h2>
              </div>

              <span className="hero-card-status">
                Live
              </span>
            </div>

            <div className="hero-card-position">
              <span>Position</span>
              <strong>President</strong>
            </div>

            <div className="hero-candidates">
              <div className="hero-candidate hero-candidate-active">
                <div className="hero-candidate-avatar">
                  A
                </div>

                <div className="hero-candidate-info">
                  <strong>Candidate A</strong>
                  <span>Leading candidate</span>
                </div>

                <span className="hero-candidate-check">
                  ✓
                </span>
              </div>

              <div className="hero-candidate">
                <div className="hero-candidate-avatar">
                  B
                </div>

                <div className="hero-candidate-info">
                  <strong>Candidate B</strong>
                  <span>Candidate</span>
                </div>
              </div>

              <div className="hero-candidate">
                <div className="hero-candidate-avatar">
                  C
                </div>

                <div className="hero-candidate-info">
                  <strong>Candidate C</strong>
                  <span>Candidate</span>
                </div>
              </div>
            </div>

            <div className="hero-card-footer">
              <span>Voting is open</span>

              <span className="hero-card-arrow">
                →
              </span>
            </div>
          </div>

          <div className="hero-floating-card hero-floating-card-top">
            <span className="hero-floating-icon">✓</span>

            <div>
              <strong>Secure</strong>
              <span>Your vote matters</span>
            </div>
          </div>

          <div className="hero-floating-card hero-floating-card-bottom">
            <span className="hero-floating-number">24</span>

            <div>
              <strong>Active</strong>
              <span>Elections</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Hero;