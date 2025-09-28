

let rootPath = "https://mysite.itvarsity.org/api/ContactBook/";
// Check for API key
let apiKey = checkApiKey();

function checkApiKey() {
    // TEMPORARY: allow index.html to load without redirect for demo
    if (!localStorage.getItem("apiKey")) {
        // window.open("enter-api-key.html", "_self");  // Commented out for demo
        return "demo-api-key"; // Dummy key so fetch works without breaking
    }
    return localStorage.getItem("apiKey");
}
