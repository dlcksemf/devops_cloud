import Review from './Review';
import ReviewForm from './ReviewForm';
import useFieldValues from 'hooks/useFieldValues';

function ReviewList() {
  const [] = useFieldValues();

  return (
    <div>
      <Review />
      <ReviewForm />
    </div>
  );
}

export default ReviewList;
