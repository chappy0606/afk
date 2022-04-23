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
    console.log(setRelics)
    setShowModal(false)
  }

  const FindRelicsByID = () => {
    const relic = relics.find((r) => r.id === relicId)
    return (
      <>
        {relic !== undefined ? (
          <>
            <label>{relic.jaName}</label>
            <label>所有数:{relic.belongings}</label>
            <label>作成数:{relic.productionCount}</label>
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
