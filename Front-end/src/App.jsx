import { useState } from 'react'
import InitPage from './components/initPage/initPage'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <InitPage/>
    </>
  )
}

export default App
