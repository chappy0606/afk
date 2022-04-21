import { Dispatch, SetStateAction } from 'react'

const Modal = (props: {
  showFlag: boolean
  setShowModal: Dispatch<SetStateAction<boolean>>
}) => {
  const closeModal = () => {
    props.setShowModal(false)
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
      {props.showFlag ? (
        <div id="overlay" style={overlay}>
          <div id="modalContent" style={modalContent}>
            <p>This is ModalContent</p>
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
