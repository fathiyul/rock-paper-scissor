import { useContext } from 'react';

import GameInfo from '../../components/game-info/game-info.component';
import OnlineGameBody from './game-body.component';
import Button from '../../components/button/button.component';
import GameRulesImage from '../../components/game-rules/game-rules.component';

import { RulesContext } from '../../contexts/rules.context';
import { SocketContext } from '../../contexts/socket.context';

const OnlineGameStart = (): JSX.Element => {
	const { isClicked, setIsClicked } = useContext(RulesContext);
	const { score } = useContext(SocketContext);

	const rulesHandler = () => setIsClicked(!isClicked);

	return (
		<div className='Game Game__Container'>
			<GameInfo score={score} />
			<OnlineGameBody />

			{isClicked ? (
				<GameRulesImage closeHandler={rulesHandler} />
			) : (
				<Button type='button' children={'rules'} handler={rulesHandler} btnStyle={'secondary'} />
			)}
		</div>
	);
};

export default OnlineGameStart;
