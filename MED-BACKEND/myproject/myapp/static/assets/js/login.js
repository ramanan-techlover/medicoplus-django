const firebaseConfig = {
  apiKey: "AIzaSyAjsLazefPpgzxXZ1MLLQ5fKF5wciS3nAk",
  authDomain: "medicoplus-cf268.firebaseapp.com",
  projectId: "medicoplus-cf268",
  storageBucket: "medicoplus-cf268.appspot.com",
  messagingSenderId: "447701321867",
  appId: "1:447701321867:web:826264e21378868146ec8e",
  measurementId: "G-W9BY50R113"
};
firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();


// Function to handle user sign-up
function handleSignUp() {
  const email = document.getElementById('signup-email').value;
  const password = document.getElementById('signup-password').value;

  firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // User signed up successfully
      const user = userCredential.user;
      console.log(`User signed up: ${user.email}`);

      /*// Define project details
      const projectName = "Your Project Name";
      const projectDescription = "Your Project Description";

      // Configure SMTP email settings and send welcome email
      Email.send({
        SecureToken: "C973D7AD-F097-4B95-91F4-40ABC5567812", // Replace with your SMTPJS API key or token
        Host: "smtp.elasticemail.com", // Replace with your SMTP server hostname
        Username: "harikishore651@gmail.com", // Your email address
        Password: "CF02FB174E9737254670C18A2318A696CAE5", // Your email password or API key
        Port: 2525, // Use the appropriate port for your SMTP server (587 for TLS, 465 for SSL)
        To: email, // Recipient's email address
        From: "harikishore651@gmail.com", // Your email address
        Subject: "WELCOME!",
        Body: "Welcome to Integrated Project Platform."
    }).then(
        message => console.log(`Email sent successfully to ${email}:`, message)
    ).catch(
        error => console.error(`Email error for ${email}:`, error)
    );*/

      // You can redirect to a dashboard or another page here
    })
    .catch((error) => {
      // Handle sign-up errors
      console.error(error.message);
    });
}


// Function to handle user sign-in
function handleSignIn() {
  const email = document.getElementById('signin-email').value;
  const password = document.getElementById('signin-password').value;

  firebase.auth().signInWithEmailAndPassword(email, password, { remember: 'local' }) // Enable persistent authentication
  .then((userCredential) => {
      // User signed in successfully
      const user = userCredential.user;
    // Check user role and redirect accordingly
    if (user) {
      window.location.href="index.html";
    } else {
      // No user signed in
      alert('Login failed. Please check your credentials.');
    }
    })
    .catch((error) => {
      // Handle sign-in errors
      console.error(error.message);
    });
}

// Event listeners for the sign-up and sign-in buttons
document.getElementById('signup-button').addEventListener('click', handleSignUp);
document.getElementById('signin-button').addEventListener('click', handleSignIn);