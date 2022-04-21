import axios from 'axios'
import { useEffect, useState } from 'react'
import Modal from 'components/modules/Modal'

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
  const [quality, setQuality] = useState<string>('Common')

  const [showModal, setShowModal] = useState<boolean>(false)

  const ShowModal = (): void => {
    setShowModal(true)
  }

  useEffect(() => {
    axios
      .get('https://192.168.10.14:8000/api/v1/relic_calculator/relics')
      .then((res) => {
        //シャローコピー
        setRelic(res.data)
      })
      .catch((error) => console.log(error.response))
  }, [])

  return (
    <>
      <button onClick={ShowModal}>showmodal</button>
      <Modal showFlag={showModal} setShowModal={setShowModal} />
      <div className="quality-nav">
        <label>
          <input
            type="radio"
            value="Common"
            checked={quality === 'Common'}
            onChange={(e) => setQuality(e.target.value)}
          />
          Common
        </label>
        <label>
          <input
            type="radio"
            value="Rare"
            checked={quality === 'Rare'}
            onChange={(e) => setQuality(e.target.value)}
          />
          Rare
        </label>
        <label>
          <input
            type="radio"
            value="Elite"
            checked={quality === 'Elite'}
            onChange={(e) => setQuality(e.target.value)}
          />
          Elite
        </label>
      </div>
      {relics
        .filter((relic) => relic.quality === quality)
        .map((relic) => (
          <img
            onClick={ShowModal}
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
