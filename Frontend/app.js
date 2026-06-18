async function sendTask() {
    const task = document.getElementById("taskInput").value;

    document.getElementById("output").innerText = "Processing...";

    try {
        const response = await fetch("http://127.0.0.1:8000/ask?question=" + task, {
            method: "POST"
        });

        const data = await response.json();
        document.getElementById("output").innerText = data.response;

    } catch (error) {
        document.getElementById("output").innerText = "Error connecting to backend";
        console.error(error);
    }
}