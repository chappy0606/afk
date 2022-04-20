import axios from 'axios'
import { useEffect, useState } from 'react'

interface Relic {
  id: string
  enName: string
  jaName: string
  quality: string
  component1: string
  component2: string
  component3: string
  component4: string
  cost: number
  totalPrice: number
  icon: string
  count: number
}

const RelicCalcuator = () => {
  const [relics, setRelic] = useState<Relic[]>([])
  useEffect(() => {
    axios
      .get('https://192.168.10.14:8000/api/v1/relic_calculator/relics')
      .then((res) => {
        setRelic(res.data)
      })
      .catch((error) => console.log(error.response))
  }, [])

  return (
    <>
      <h2>聖物計算機</h2>
      {relics.map((relic) => (
        <img
          key={relic.id}
          src={relic.icon}
          alt={relic.jaName}
          width="50"
          height="50"
        ></img>
      ))}
    </>
  )
}

export default RelicCalcuator