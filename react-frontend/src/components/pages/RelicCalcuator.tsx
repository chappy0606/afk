import axios, { AxiosResponse, AxiosError } from 'axios'
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
  productionCount: number
  belongings: number
  icon: string
}

const RelicCalcuator = () => {
  const [relics, setRelics] = useState<Relic[]>([])
  const [quality, setQuality] = useState<string>('Common')
  const [showModal, setShowModal] = useState<boolean>(false)
  const [relicId, setRelicId] = useState<string>('')

  const ShowModal = () => {
    setShowModal(true)
  }

  const test = () => {
    const copyRelics = JSON.parse(
      JSON.stringify(relics.filter((v) => v.productionCount !== v.belongings)),
    ) as Relic[]

    copyRelics.map((v) => {
      const diff: number = v.productionCount - v.belongings

      return diff > 0
        ? { ...v, productionCount: diff, belongings: 0 }
        : { ...v, productionCount: 0, belongings: Math.abs(diff) }
    })
  }

  useEffect(() => {
    axios
      .get('https://192.168.10.14:8000/api/v1/relic_calculator/relics')
      .then((res: AxiosResponse<Relic[]>) => {

        setRelics(
          res.data.map((r) => ({ ...r, productionCount: 0, belongings: 0 })),
        )
      })
      .catch((error: AxiosError) => console.log(error.response))
  }, [])

  return (
    <>
      <div className="quality-nav">
        <label htmlFor="Common">
          Common
          <input
            type="radio"
            value="Common"
            id="Common"
            checked={quality === 'Common'}
            onChange={(e) => setQuality(e.target.value)}
          />
        </label>
        <label htmlFor="Rare">
          Rare
          <input
            type="radio"
            value="Rare"
            id="Rare"
            checked={quality === 'Rare'}
            onChange={(e) => setQuality(e.target.value)}
          />
        </label>
        <label htmlFor="Elite">
          Elite
          <input
            type="radio"
            value="Elite"
            id="Elite"
            checked={quality === 'Elite'}
            onChange={(e) => setQuality(e.target.value)}
          />
        </label>
      </div>
      <Modal
        showFlag={showModal}
        setShowModal={setShowModal}
        relics={relics}
        setRelics={setRelics}
        relicId={relicId}
      />
      {relics
        .filter((relic) => relic.quality === quality)
        .map((relic) => (
          <button type="button" id="img-wrapper-btn" key={relic.id}>
            <img
              src={relic.icon}
              alt={relic.jaName}
              width="50"
              height="50"
              role="presentation"
              onClick={() => {
                setRelicId(relic.id)
                ShowModal()
              }}
            />
          </button>
        ))}
      <h3>合計エッセンス</h3>
      <h3>不必要な遺物</h3>
      {test()}
    </>
  )
}

export default RelicCalcuator
