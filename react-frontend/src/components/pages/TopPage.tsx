import { Link } from 'react-router-dom'

const TopPage = () => {
  return (
    <>
      <div className="top-page">
        <h1 className="logo">
          <img src="/logo.png" alt="AFK" />
        </h1>
        <div className="menubar">
          <li>
            <Link to="/RelicCalcuator">RelicCalcuator</Link>
          </li>
        </div>
      </div>
    </>
  )
}
export default TopPage