import List from "./List";
import UserGreeting from "./userGreeting";

function App() {
  const fruits = [
    {id: 1, name:'Apple', calories: 95},
    {id: 2, name:'Orange', calories: 45 },
    {id: 3, name:'Banana', calories: 105},
    {id: 4, name:'Coconut', calories: 159},
    {id: 5, name:'Pineapple', calories: 37 }];

  const vegetables = [
    {id: 1, name:'potatoes', calories: 110},
    {id: 2, name:'celery', calories: 15 },
    {id: 3, name:'carrots', calories: 25},
    {id: 4, name:'corn', calories: 65},
    {id: 5, name:'brocoli', calories: 50 }];
  return(
    <>
    {fruits.length > 0 && <List items={fruits} category='Fruits'/>}
    {vegetables.length > 0 && <List  items={vegetables} category='Vegetables'/>}
    </>
  );
}

export default App
