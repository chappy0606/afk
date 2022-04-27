import { Relic } from 'components/pages/RelicCalcuator'
import { Dispatch, SetStateAction } from 'react'

const Modal = (props: {
  showFlag: boolean
  setShowModal: Dispatch<SetStateAction<boolean>>
  relics: Relic[]
  setRelics: Dispatch<SetStateAction<Relic[]>>
  relicId: string
}) => {
  const { showFlag, setShowModal, relics, setRelics, relicId } = props

  const closeModal = () => {
    setShowModal(false)
  }

  const Increment = (e: { currentTarget: HTMLButtonElement }, relic: Relic) => {
    const key = e.currentTarget.name as keyof typeof relic
    const copy: Relic[] = JSON.parse(JSON.stringify(relics))

    const newState = copy.map((v) => {
      if (v.id === relic.id) {
        v[key]++
      }
      return v
    })
    setRelics(newState)
  }

  const Decrement = (e: { currentTarget: HTMLButtonElement }, relic: Relic) => {
    const key = e.currentTarget.name as keyof typeof relic
    const copy: Relic[] = JSON.parse(JSON.stringify(relics))

    const newState = copy.map((v) => {
      if (v.id === relic.id && v[key] > 0) {
        v[key]--
      }
      return v
    })
    setRelics(newState)
  }

  const FindRelicsByID = () => {
    const relic: Relic = JSON.parse(
      JSON.stringify(relics.find((r) => r.id === relicId)),
    )

    return (
      <>
        {relic !== undefined ? (
          <>
            <label>{relic.jaName}</label>
            <div className="">
              <label>所有数:{relic.belongings}</label>
              <button name="belongings" onClick={(e) => Increment(e, relic)}>
                +
              </button>
              <button name="belongings" onClick={(e) => Decrement(e, relic)}>
                -
              </button>
            </div>

            <label>作成数:{relic.productionCount}</label>
            <button name="productionCount" onClick={(e) => Increment(e, relic)}>
              +
            </button>
            <button name="productionCount" onClick={(e) => Decrement(e, relic)}>
              -
            </button>
            <img src={relic.icon} alt={relic.jaName} width="50" height="50" />
          </>
        ) : (
          <></>
        )}
      </>
    )
  }

  //React.CSSPropertiesの型指定ないとエラー吐く
  const modalContent: React.CSSProperties = {
    background: 'white',
    padding: '10px',
    borderRadius: '3px',
  }

  const overlay: React.CSSProperties = {
    position: 'fixed',
    top: 0,
    left: 0,
    width: '100%',
    height: '100%',
    backgroundColor: 'rgba(0,0,0,0.5)',

    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  }
  return (
    <>
      {showFlag ? (
        <div id="overlay" style={overlay}>
          <div id="modalContent" style={modalContent}>
            {FindRelicsByID()}
            <button onClick={closeModal}>Close</button>
          </div>
        </div>
      ) : (
        <></>
      )}
    </>
  )
}

export default Modal
