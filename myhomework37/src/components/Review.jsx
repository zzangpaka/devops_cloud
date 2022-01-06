import { useState } from 'react/cjs/react.development';
import Rate from './Rate';

function Review({ review, handleEdit, handleDelete }) {
  const [showMenu, setShowMenu] = useState(false);

  const handleEditButton = () => {
    if (handleEdit) {
      handleEdit();
    } else {
      console.warn('[Review] handleEdit 속성값이 지정되지 않았습니다.');
    }
  };

  const handleDeleteButton = () => {
    if (handleDelete) {
      handleDelete();
    } else {
      console.warn('[Review] handleDelete 속성값이 지정되지 않았습니다.');
    }
  };

  return (
    <div
      onMouseEnter={() => setShowMenu(true)}
      onMouseLeave={() => setShowMenu(false)}
      className="bg-white my-1 p-1 pt-3
      border-2 border-gray-500 
      hover:bg-gray-100 relative"
    >
      {showMenu && (
        <div className="text-xs absolute top-0 right-0">
          <span
            className="hover:text-pink-600 cursor-pointer mr-1"
            onClick={handleEditButton}
          >
            수정
          </span>
          <span
            className="hover:text-pink-600 cursor-pointer"
            onClick={handleDeleteButton}
          >
            삭제
          </span>
        </div>
      )}

      {review.content.split('\n').map((line) => (
        <>
          {line}
          <br />
          <Rate rate={review.rate} />
        </>
      ))}
    </div>
  );
}

export default Review;
