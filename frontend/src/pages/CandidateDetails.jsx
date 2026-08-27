import { Link, useParams } from "react-router-dom";

import "./CandidateDetails.css";

function CandidateDetails() {
  const { electionId, candidateId } = useParams();

  return (
    <main className="candidate-details-page">
      <section className="candidate-details-container">
        <Link
          to={`/elections/${electionId}`}
          className="candidate-back-link"
        >
          ← Back to Election
        </Link>

        <div className="candidate-profile-card">
          <div className="candidate-profile-image">
            <img
              src="/src/assets/votera-logo.png"
              alt="Candidate"
            />
          </div>

          <div className="candidate-profile-content">
            <span className="candidate-eyebrow">
              CANDIDATE PROFILE
            </span>

            <h1>Candidate Details</h1>

            <p className="candidate-position">
              Candidate ID: {candidateId}
            </p>

            <p className="candidate-description">
              More information about this candidate will appear here.
              This page will eventually contain the candidate's
              biography, experience, manifesto, and voting information.
            </p>

            <button type="button" className="candidate-vote-button">
              Vote for Candidate
            </button>
          </div>
        </div>
      </section>
    </main>
  );
}

export default CandidateDetails;