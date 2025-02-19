import './initPage.css'
import InitButton from '../initButton/InitButton'


const InitPage = () =>{
    return(
        <div className='init-main'>
            <section className='main-left'>
                <h2>Welcome to the</h2>
                <h1>Solve-Together</h1>
                <div className='img-cubeman'></div>
            </section>
            <section className='main-right'>
                <p>Pulse-Together is a cooperative game where you can solve Rubik's Cubes together with other players. Currently, only the 3x3 cube is available. No account is required to play – just share the link or join a random room to get started.</p>
                <InitButton text='Play with Friend'/>
                <InitButton text='Play with Random'/>
            </section>
        </div>
    )
}
export default InitPage