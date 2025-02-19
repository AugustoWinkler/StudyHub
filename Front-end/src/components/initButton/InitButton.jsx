import './initButton.css'


const InitButton = (props) => {
    return(
        <article class="Border006">
            <span class="top006"></span>
            <span class="right006"></span>
            <span class="bottom006"></span>
            <span class="left006"></span>
            <h1>{props.text}</h1>
        </article>
    )
}
export default InitButton