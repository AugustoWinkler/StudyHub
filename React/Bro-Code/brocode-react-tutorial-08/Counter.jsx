//updater function = a function passe as argument to setState() ussualy
//                   ex: setYear(year+1)
//                   allow for safe updates based on the previous state use with multiple state updates and asynchrono functions
//                   Good practice to use updater function

import React,{useState} from 'react';
function Counter () {
    const [count, setCount] = useState(0);

    const increment = () => {
        //c = prevCount
        setCount(c => c +1);
     
       
    }
    const decrement = () => {
        //c = prevCount
        setCount(c => c-1);
    }
    const reset = () =>{
        setCount(0);
    }
    return(
        <div className='counter-container'>
            <p className='counter-display'>{count}</p>
            <button className='counter-button' onClick={decrement}>Decrement</button>
            <button className='counter-button' onClick={reset}>Reset</button>
            <button className='counter-button' onClick={increment}>Increment</button>
        </div>
    )
}
export default Counter