import profilepic from './assets/perfil.jpg'
function Card(){
    return(
        <div className="Card">
            <img className='CardImage' src={profilepic} alt="profile picture"></img>
            <h2 className='Card-Tittle'>Augusto Winkler</h2>
            <p className='Card-Text'>Software Engineer Student</p>
        </div>
    );
}
export default Card