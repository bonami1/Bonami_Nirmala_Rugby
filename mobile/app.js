async function getTeams() {
    const reponse = await fetch("http://127.0.0.1:8000/api/teams", {
        method: "GET",
        headers: {"Content-type": "application/json"},
    });
    return await reponse.json();
}

async function getStadiums() {
    const reponse = await fetch("http://127.0.0.1:8000/api/stadiums", {
        method: "GET",
        headers: {"Content-type": "application/json"},
    });
    return await reponse.json();
}

async function getEvents() {
    const reponse = await fetch("http://127.0.0.1:8000/api/events", {
        method: "GET",
        headers: {"Content-type": "application/json"},
    });
    return await reponse.json();
}


async function eventsDetails(id) {
    try {
        let rep = await fetch("http://127.0.0.1:8000/api/eventsDetails/" + id, {
            method: "GET",
        });
        let reponse = await rep.json();
        console.log("RESULT EVENTS DETAILS : ", reponse);
        return reponse;
    } catch (error) {
        console.error("Error : ", error);
        throw error; 
    }
}

let divContenu = document.getElementById("contenu")
async function afficherEventsDetails() {
    const events = await getEvents();
    const stadiums = await getStadiums();
    const teams = await getTeams();

    events.RESULT.forEach(event => {
        //const eventId = event.pk;
        const stadId = event.stadium;
        const teamHomeId = (event.team_home);
        const teamAwayId = (event.team_away);
        const start = event.start;

        const stadFind = stadiums.RESULT.find(stadium => stadium.id === stadId);
        // const teamHomeDetails = teams.RESULT[teamHomeId];
        // const teamAwayDetails = teams.RESULT[teamAwayId];  recup avec l'index
        const teamHome = teams.RESULT.find(team => team.id === teamHomeId); // recup avec l'id
        const teamAway = teams.RESULT.find(team => team.id === teamAwayId);

        if (teamHome === null || teamAway.country === null) {
            const displayEventInfos = document.createElement("p");
            displayEventInfos.textContent = `Conditions // stadium name ${stadFind.name}, team home : ? , team away ? , start ${start}`;
            divContenu.appendChild(displayEventInfos);
        } else {
            const displayStad = document.getElementById("stad");
            displayStad.textContent = `STADIUM : ${stadFind.name}`;
            

            const displayTeamHome = document.getElementById("teamHome");
            displayTeamHome.textContent = `TEAM HOME : ${teamHome.country}`;

            const displayTeamAway = document.getElementById("teamAway");
            displayTeamAway.textContent = `TEAM AWAY : ${teamAway.country}`;

            const displayDate = document.getElementById("date");
            displayDate.textContent = `DATE : ${start}`;
            divContenu.appendChild(displayStad, displayTeamHome, displayTeamAway, displayDate);        

            const displayEventInfos = document.createElement("p");
            displayEventInfos.textContent = `EVENTS // stadium name: ${stadFind.name}, team home: ${teamHome.country}, team away: ${teamAway.country}, start: ${start}`;
            divContenu.appendChild(displayEventInfos);
        }
    });
}


afficherEventsDetails();