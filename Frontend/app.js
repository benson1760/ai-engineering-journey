async function sendTask() {
    const task = document.getElementById("taskInput").value;

    document.getElementById("output").innerText = "Processing...";

    // This will connect to your backend later
    document.getElementById("output").innerText =
        "Agent response will appear here.";
}