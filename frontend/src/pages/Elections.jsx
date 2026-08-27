import { useMemo, useState } from "react";
import ElectionCard from "../components/ElectionCard/ElectionCard";
import "./Elections.css";
import CandidateCard from "../components/CandidateCard/CandidateCard";

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
  },
  {
    id: 3,
    title: "Engineering Students Election",
    organization: "Engineering Students Association",
    description:
      "Participate in the election and choose your preferred representatives.",
    image: "/src/assets/votera-logo.png",
    status: "Closed",
    startDate: "Jul 10, 2026",
    endDate: "Jul 18, 2026",
  },
];

function Elections() {
  const [searchTerm, setSearchTerm] = useState("");
  const [activeFilter, setActiveFilter] = useState("All");

  const filteredElections = useMemo(() => {
    return elections.filter((election) => {
      const matchesSearch =
        election.title
          .toLowerCase()
          .includes(searchTerm.toLowerCase()) ||
        election.organization
          .toLowerCase()
          .includes(searchTerm.toLowerCase());

      const matchesFilter =
        activeFilter === "All" ||
        election.status === activeFilter;

      return matchesSearch && matchesFilter;
    });
  }, [searchTerm, activeFilter]);

  return (
    <main className="elections-page">
      <section className="elections-header">
        <div className="elections-header-content">
          <span className="elections-eyebrow">
            VOTERA ELECTIONS
          </span>

          <h1>Find an Election</h1>

          <p>
            Discover active and upcoming elections and make
            your voice count.
          </p>
        </div>
      </section>

      <section className="elections-controls">
        <div className="elections-search">
          <span className="search-icon">⌕</span>

          <input
            type="text"
            placeholder="Search elections..."
            value={searchTerm}
            onChange={(event) =>
              setSearchTerm(event.target.value)
            }
          />
        </div>

        <div className="election-filters">
          {["All", "Live", "Upcoming", "Closed"].map(
            (filter) => (
              <button
                key={filter}
                className={
                  activeFilter === filter
                    ? "filter-button active"
                    : "filter-button"
                }
                onClick={() => setActiveFilter(filter)}
              >
                {filter}
              </button>
            )
          )}
        </div>
      </section>

      <section className="elections-results">
        {filteredElections.length > 0 ? (
          <div className="elections-grid">
            {filteredElections.map((election) => (
              <ElectionCard
                key={election.id}
                election={election}
              />
            ))}
          </div>
        ) : (
          <div className="elections-empty">
            <div className="empty-icon">⌕</div>

            <h2>No elections found</h2>

            <p>
              We couldn't find any elections matching your
              search or selected filter.
            </p>

            <button
              className="clear-filters"
              onClick={() => {
                setSearchTerm("");
                setActiveFilter("All");
              }}
            >
              Clear filters
            </button>
          </div>
        )}
      </section>
    </main>
  );
}

export default Elections;