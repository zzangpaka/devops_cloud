import useFieldValues from 'hooks/useFieldValues';
import { useState } from 'react';
import Review from './Review';
import ReviewForm from './ReviewForm';
import './ReviewList.css';

const INITIAL_STATE = [
  { id: 1, content: '추천함', rate: '5' },
  { id: 2, content: '비추천', rate: '1' },
  { id: 3, content: '그냥그럼', rate: '3' },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);
  const [changePage, setChangePage] = useState(false);
  const [fieldValues, handleChange, clearFieldValues, setFieldValues] =
    useFieldValues({
      content: '',
      rate: '0',
    });

  const appendReview = () => {
    let { id: reviewId } = fieldValues;

    if (!reviewId) {
      reviewId = new Date().getTime();
      const createdReview = { ...fieldValues, id: reviewId };
      setReviewList((prevReviewList) => [...prevReviewList, createdReview]);
    } else {
      const editedReview = { ...fieldValues };
      setReviewList((prevReviewList) =>
        prevReviewList.map((review) => {
          return review.id === editedReview.id ? editedReview : review;
        }),
      );
    }

    setChangePage(false);
    clearFieldValues();
  };

  const willeditReview = (editingReview) => {
    console.log('Editing', editingReview);
    setFieldValues(editingReview);
    setChangePage(true);
  };

  const deleteReview = (deletingReview) => {
    setReviewList((prevReviewList) =>
      prevReviewList.filter(({ id }) => id !== deletingReview.id),
    );
  };

  return (
    <div className="review-list">
      <h1 className="text-xl mb-2 border-b-2 border-pink-500">Review List</h1>
      {changePage && (
        <ReviewForm
          fieldValues={fieldValues}
          handleSubmit={appendReview}
          handleChange={handleChange}
        />
      )}
      {!changePage && (
        <button
          className="bg-red-100 
          hover:bg-red-300 p-1 
          rounded text-sm"
          onClick={() => setChangePage((prevState) => !prevState)}
        >
          새 리뷰 쓰기
        </button>
      )}
      {/* <hr />
      {JSON.stringify(fieldValues)} */}
      {reviewList.map((review) => (
        <Review
          handleEdit={() => willeditReview(review)}
          handleDelete={() => deleteReview(review)}
          review={review}
          key={review.id}
        />
      ))}
    </div>
  );
}

export default ReviewList;
