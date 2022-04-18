import './App.css'
import { BrowserRouter, Route, Routes, Link } from 'react-router-dom'

const App = () => {
  return (
    <>
      <div className="App">
        <BrowserRouter>
          <div className="render">
            <Link to="/Page1">
              <button type="button">Page1</button>
            </Link>
          </div>
          <Routes>
            <Route path="/" element={<Top />} />
            <Route path="/Page1" element={<Page1 />} />
          </Routes>
        </BrowserRouter>
      </div>
    </>
  )
}

const Top = () => {
  return <h2>Home</h2>
}
const Page1 = () => {
  return <h2>Page1</h2>
}

export default App
