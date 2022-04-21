import axios from 'axios'
import { useEffect, useState } from 'react'
import Modal from 'components/modules/Modal'

export interface Relic {
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
}

const RelicCalcuator = () => {
  const [relics, setRelics] = useState<Relic[]>([])
  const [relic, setRelic] = useState<Relic>({
    id: '1',
    enName: '',
    jaName: '',
    quality: '',
    component1: '',
    component2: '',
    component3: '',
    component4: '',
    cost: 0,
    totalPrice: 0,
    icon: '',
  })
  const [quality, setQuality] = useState<string>('Common')
  const [showModal, setShowModal] = useState<boolean>(false)

  const ShowModal = (relic: Relic) => {
    setShowModal(true)
    setRelic(relic)
  }

  useEffect(() => {
    axios
      .get('https://192.168.10.14:8000/api/v1/relic_calculator/relics')
      .then((res) => {
        //シャローコピー
        setRelics(res.data)
      })
      .catch((error) => console.log(error.response))
  }, [])

  return (
    <>
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

      <Modal showFlag={showModal} setShowModal={setShowModal} relic={relic} />
      {relics
        .filter((relic) => relic.quality === quality)
        .map((relic) => (
          <img
            key={relic.id}
            src={relic.icon}
            alt={relic.jaName}
            width="50"
            height="50"
            onClick={() => ShowModal(relic)}
          ></img>
        ))}
    </>
  )
}

export default RelicCalcuator
