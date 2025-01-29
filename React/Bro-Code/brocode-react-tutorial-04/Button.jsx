function Button(){
    const handleClick = (event) => event.target.textContent = 'Ouch 🤣'

    
    return(
        <button  onDoubleClick={(event) => handleClick(event)}>Click-me 😳</button>
    )

}
export default Button