import 'Circle.css';

function Circle({ number, backgroundColor, onClick, onContext }) {
  return (
    <div
      className="circle"
      style={{ backgroundColor }}
      onClick={onClick}
      onContextMenu={onContext}
    >
      {number}
    </div>
  );
}

export default Circle;
