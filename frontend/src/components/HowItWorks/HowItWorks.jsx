import "./HowItWorks.css";

function HowItWorks() {
  return (
    <section className="how-it-works" id="how-it-works">
      <div className="how-it-works-container">

        <div className="how-it-works-header">
          <span className="section-eyebrow">
            HOW IT WORKS
          </span>

          <h2>
            Voting should be simple.
          </h2>

          <p>
            From finding an election to seeing the results,
            Votera keeps the entire voting experience clear and
            straightforward.
          </p>
        </div>

        <div className="steps-container">

          <div className="step-card">
            <div className="step-number">
              01
            </div>

            <div className="step-icon">
              <span>⌕</span>
            </div>

            <h3>
              Find an Election
            </h3>

            <p>
              Find the election you want to participate in and
              view its positions, candidates, and voting details.
            </p>
          </div>

          <div className="step-connector" />

          <div className="step-card">
            <div className="step-number">
              02
            </div>

            <div className="step-icon">
              <span>✓</span>
            </div>

            <h3>
              Make Your Choice
            </h3>

            <p>
              Review the available candidates and cast your vote
              through a simple and intuitive voting experience.
            </p>
          </div>

          <div className="step-connector" />

          <div className="step-card">
            <div className="step-number">
              03
            </div>

            <div className="step-icon">
              <span>↗</span>
            </div>

            <h3>
              See the Results
            </h3>

            <p>
              Once the election closes, results can be counted
              and presented clearly to authorized users.
            </p>
          </div>

        </div>

      </div>
    </section>
  );
}

export default HowItWorks;