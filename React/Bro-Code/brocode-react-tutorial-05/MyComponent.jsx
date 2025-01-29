import React, {useState} from 'react';

function MyComponent (){
    const [name, setName] = useState("Guest");
    const [age, setAge] = useState(0);
    const [isEmployed,setIsEmployed] = useState(false);
    const updateName = () =>{
        setName("SpongeBob")
    }

    const incrementAge = () =>{
        setAge(age+1);
    }
    
    const toggleEmployedStatus = () => {
        setIsEmployed(!isEmployed);
    }
    
    return(
        <div>
            <p>Name: {name}</p>
            <button onClick={updateName}>Set Name</button>

            <p>Age: {age}</p>
            <button onClick={incrementAge}>IToggle Status</button>

            <p>is employed: {isEmployed ? "Yes" : "No"}</p>
            <button onClick={toggleEmployedStatus}>Increment Age</button>
        </div>
    );
}
export default MyComponent