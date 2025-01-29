import PropTypes from 'prop-types'

function UserGreeting (props){

    const welcomeMessage = <h2 className="welcome-message">Welcome {props.username}</h2>
    const logginPrompt = <h2 className="loggin-prompt">Please Log In to Continue.</h2>

   return(props.isLoggedIn ? welcomeMessage : logginPrompt)
}
UserGreeting.proptypes = {
    isLoggedIn: PropTypes.bool,
    username: PropTypes.string,
}
UserGreeting.defaultProps = {
    isLoggedIn: false,
    username: 'Guest',
}

export default UserGreeting