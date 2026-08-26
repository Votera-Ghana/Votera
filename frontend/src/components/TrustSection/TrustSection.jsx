import "./TrustSection.css";

function TrustSection() {
  return (
    <section className="trust-section">
      <div className="trust-container">

        <div className="trust-heading">
          <span className="trust-badge">WHY VOTERA</span>

          <h2>
            Built for elections
            <span> that matter.</span>
          </h2>

          <p>
            Votera makes digital voting simple, transparent, and reliable
            for organizations, universities, schools, clubs, and associations.
          </p>
        </div>

        <div className="trust-grid">

          <div className="trust-card">
            <div className="trust-icon">✓</div>

            <div>
              <h3>Secure Voting</h3>
              <p>
                Every vote is handled through a secure and carefully designed
                voting experience.
              </p>
            </div>
          </div>

          <div className="trust-card">
            <div className="trust-icon">◈</div>

            <div>
              <h3>Transparent Results</h3>
              <p>
                Clear results help organizations understand election outcomes
                with confidence.
              </p>
            </div>
          </div>

          <div className="trust-card">
            <div className="trust-icon">↗</div>

            <div>
              <h3>Easy to Use</h3>
              <p>
                A straightforward experience makes it easy for voters to find
                elections and make their choices.
              </p>
            </div>
          </div>

        </div>

        <div className="trust-stat">
          <div className="trust-stat-number">24+</div>

          <div className="trust-stat-content">
            <strong>Active Elections</strong>
            <span>and more organizations joining Votera</span>
          </div>
        </div>

      </div>
    </section>
  );
}

export default TrustSection;