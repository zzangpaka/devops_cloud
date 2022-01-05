import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Review from './Review';
import ReviewForm from './ReviewForm';
import './ReviewList.css';

const INITIAL_STATE = [
  { content: '추천함', rate: '5' },
  { content: '비추천', rate: '1' },
  { content: '그냥그럼', rate: '3' },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  // const [changePage, setChangePage] = useState(false);
  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    content: '',
    rate: '0',
  });

  const removeReview = (reviewIndex) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter((_, index) => index !== reviewIndex),
    );
  };

  const appendReview = () => {
    const review = { ...fieldValues };

    setReviewList((prevReviewList) => [...prevReviewList, review]);
    // setChangePage((prevState) => !prevState);

    clearFieldValues();
  };

  return (
    <div className="review-list">
      <h1 className="text-xl mb-2 border-b-2 border-pink-500">Review List</h1>
      {/* {changePage && (
        <ReviewForm
          fieldValues={fieldValues}
          handleSubmit={appendReview}
          handleChange={handleChange}
        />
      )}
      {!changePage && ( */}
      <button
        className="bg-red-100 
        hover:bg-red-300 p-1 
        rounded text-sm"
        // onClick={() => setChangePage((prevState) => !prevState)}
      >
        새 리뷰 쓰기
      </button>
      {/* )} 찬들 교육생 코드를 참고해 리뷰 폼이 숨었다 나타났다 할 수 있게 구현은 했지만 로직이 이해가 되지 않아서 주석처리 합니다..... */}

      <ReviewForm
        fieldValues={fieldValues}
        handleChange={handleChange}
        handleSubmit={appendReview}
      />
      {/* <hr />
      {JSON.stringify(fieldValues)} */}
      {reviewList.map((review, index) => (
        <Review
          review={review}
          key={index}
          onClick={() => removeReview(index)}
        />
      ))}
    </div>
  );
}

export default ReviewList;
