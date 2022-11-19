import React, { useState } from "react";

import "./SignupForm.css";

function SignupForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function handleNameChange(event) {
    setName(event.target.value);
  }
  function handleEmailChange(event) {
    setEmail(event.target.value);
  }
  function handlePasswordChange(event) {
    setPassword(event.target.value);
  }
  async function sendSignupData() {
    const data = {
      name,
      email,
      password,
    };
    const response = await fetch("http://127.0.0.1:8000/signup/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    console.log(response);
  }
  function handleSubmit(event) {
    event.preventDefault();
    sendSignupData();
    setName("");
    setEmail("");
    setPassword("");
  }

  return (
    <form action="" onSubmit={handleSubmit} className="signup-form">
      <h1>Sign Up</h1>
      <input
        type="text"
        name=""
        id="name-input"
        onChange={handleNameChange}
        value={name}
        placeholder="Enter your name"
      />
      <input
        type="email"
        name=""
        id="email-input"
        onChange={handleEmailChange}
        value={email}
        placeholder="Enter your email"
      />
      <input
        type="password"
        name=""
        id="pass-input"
        onChange={handlePasswordChange}
        value={password}
        placeholder="Enter password"
      />
      <button type="submit">Submit</button>
    </form>
  );
}

export default SignupForm;
