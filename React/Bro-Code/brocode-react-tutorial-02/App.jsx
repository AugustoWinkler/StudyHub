import Card from './Card.jsx'
import Student from './Students.jsx';



function App() {
  return(
    <>
    <Student name='Sponge Bob' age={30} isStudent={true}/>
    <Student name='Pratick' age={42} isStudent={false} />
    <Student name='Squidward' age={50} isStudent={false} />
    <Student name='Sandy' age={27} isStudent={true} />
    <Student name='Larry'/>
    </> 
  );
}
export default App
