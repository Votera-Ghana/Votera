import { useParams, Link } from "react-router-dom";
import { useState } from "react";

import CandidateCard from "../components/CandidateCard/CandidateCard";

import "./ElectionDetails.css";

const elections = [
  {
    id: 1,
    title: "SRC Election 2026",
    organization: "Student Representative Council",
    description:
      "Choose the next student representatives for the 2026 academic year.",
    image: "/src/assets/votera-logo.png",
    status: "Live",
    startDate: "Aug 20, 2026",
    endDate: "Aug 30, 2026",
    positions: [
      {
        title: "SRC President",
        candidates: [
          {
            id: 1,
            name: "Candidate One",
            image: "/src/assets/votera-logo.png",
            bio: "A dedicated student leader passionate about representation and student welfare.",
          },
          {
            id: 2,
            name: "Candidate Two",
            image: "/src/assets/votera-logo.png",
            bio: "Committed to building a stronger and more inclusive student community.",
          },
        ],
      },
      {
        title: "General Secretary",
        candidates: [
          {
            id: 3,
            name: "Candidate Three",
            image: "/src/assets/votera-logo.png",
            bio: "Focused on communication, accountability and student engagement.",
          },
          {
            id: 4,
            name: "Candidate Four",
            image: "/src/assets/votera-logo.png",
            bio: "Passionate about improving the student experience.",
          },
        ],
      },
    ],
  },
  {
    id: 2,
    title: "Computer Science Association Election",
    organization: "Computer Science Association",
    description:
      "Vote for the leaders who will represent the association.",
    image: "/src/assets/votera-logo.png",
    status: "Upcoming",
    startDate: "Sep 5, 2026",
    endDate: "Sep 12, 2026",
    positions: [
      {
        title: "Association President",
        candidates: [
          {
            id: 5,
            name: "Candidate Five",
            image: "/src/assets/votera-logo.png",
            bio: "Dedicated to serving students and strengthening the association.",
          },
          {
            id: 6,
            name: "Candidate Six",
            image: "/src/assets/votera-logo.png",
            bio: "Committed to innovation, collaboration and student development.",
          },
        ],
      },
    ],
  },
];

function ElectionDetails() {
  const { electionId } = useParams();
  const [voteAmounts, setVoteAmounts] = useState({});
  const [ballot, setBallot] = useState([]);

  const handleAmountChange = (candidateName, amount) => {
  setVoteAmounts((current) => ({
    ...current,
    [candidateName]: amount,
  }));
};

const addVote = (candidate, position) => {
  const amount = Number(voteAmounts[candidate.name] || 0);

  if (amount <= 0) {
    return;
  }

  const votes = amount * 10;

  setBallot((current) => [
    ...current,
    {
      candidate: candidate.name,
      position: position.title,
      amount,
      votes,
    },
  ]);

  setVoteAmounts((current) => ({
    ...current,
    [candidate.name]: "",
  }));
};


  const election = elections.find(
    (item) => item.id === Number(electionId)
  );

  if (!election) {
    return (
      <main className="election-details-page">
        <section className="election-not-found">
          <span className="not-found-icon">!</span>

          <h1>Election not found</h1>

          <p>
            The election you are looking for does not exist
            or is no longer available.
          </p>

          <Link to="/elections" className="back-button">
            Back to Elections
          </Link>
        </section>
      </main>
    );
  }

  return (
    <main className="election-details-page">

      <section className="election-details-hero">
        <Link to="/elections" className="back-link">
          ← Back to Elections
        </Link>

        <div className="election-overview">

          <div className="election-image-wrapper">
            <img
              src={election.image}
              alt={election.title}
              className="election-details-image"
            />
          </div>

          <div className="election-overview-content">

            <span
              className={`election-status ${election.status.toLowerCase()}`}
            >
              {election.status}
            </span>

            <span className="election-organization">
              {election.organization}
            </span>

            <h1>{election.title}</h1>

            <p className="election-description">
              {election.description}
            </p>

            <div className="election-dates">
              <div>
                <span>Starts</span>
                <strong>{election.startDate}</strong>
              </div>

              <div>
                <span>Ends</span>
                <strong>{election.endDate}</strong>
              </div>
            </div>

          </div>
        </div>
      </section>


      <section className="positions-section">

        <div className="positions-header">
          <span className="section-eyebrow">
            ELECTION POSITIONS
          </span>

          <h2>Choose your candidates</h2>

          <p>
            Select a candidate for each position and cast
            your vote.
          </p>
        </div>


        <div className="positions-list">

          {election.positions.map((position) => (
            <article
              className="position-card"
              key={position.title}
            >

              <div className="position-heading">
                <span className="position-number">
                  {election.positions.indexOf(position) + 1}
                </span>

                <div>
                  <span>POSITION</span>
                  <h3>{position.title}</h3>
                </div>
              </div>


              <div className="candidates-grid">
                {position.candidates.map((candidate) => (
                  <CandidateCard
                    key={candidate.id || candidate.name}
                    candidate={candidate}
                    position={position.title}
                    electionId={election.id}
                  />
                ))}
              </div>

            </article>
          ))}

        </div>

        {ballot.length > 0 && (
            <div className="ballot-summary">

                <div className="ballot-header">
                <span className="section-eyebrow">
                    YOUR BALLOT
                </span>

                <h2>Vote Summary</h2>

                <p>
                    Review the votes you have added before
                    proceeding to payment.
                </p>
                </div>

                <div className="ballot-list">
                {ballot.map((vote, index) => (
                    <div
                    className="ballot-item"
                    key={`${vote.candidate}-${index}`}
                    >
                    <div>
                        <strong>{vote.candidate}</strong>
                        <span>{vote.position}</span>
                    </div>

                    <div className="ballot-votes">
                        <strong>{vote.votes} votes</strong>
                        <span>GHS {vote.amount}</span>
                    </div>
                    </div>
                ))}
                </div>

            </div>
            )}

      </section>

    </main>
  );
}

export default ElectionDetails;