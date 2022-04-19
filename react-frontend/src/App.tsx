import { BrowserRouter, Route, Routes } from 'react-router-dom'
import TopPage from 'components/pages/TopPage'
import RelicCalcuator from 'components/pages/RelicCalcuator'

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<TopPage />} />
        <Route path="/RelicCalcuator" element={<RelicCalcuator />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
