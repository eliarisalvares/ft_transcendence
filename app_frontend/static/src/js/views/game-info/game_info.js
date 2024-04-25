import gameInfoService from '../../services/gameInfoService.js';

import View, { ViewOptions } from '../../contracts/view.js';
import NavHandler from '../../router/navigation/navHandler.js';
import { NavItems } from '../../router/navigation/navItem.js';

class GameInfoView extends View {
  constructor(
    html,
    start
  ) {
    const navItems = [
      new NavItems('#game-info', 'Dahboard'),
    ];
    const navHandler = new NavHandler(navItems);
    super(new ViewOptions(html, start, navHandler));
  }
}

const html = /*html*/`
  <div class="container-fluid main">
        <div class="containers">
            <div class="row">
                <div class="col-lg-12 mb-3">
                    <div class="container_details text-center">
                        <div class="row align-items-center justify-content-center">
                            <div class="col-md-4">
                                <img src="static/src/img/gold_medal_star_icon.png" alt="medalha do usuário" class="details-pictures details-medal-picture">
                                <p class="mb-1">Shelson Alves</p>
                                <p><i class="fa-solid fa-circle me-2" style="color: green;"></i>Online</p>
                            </div>
                            <div class="col-md-4">
                                <img src="static/src/img/avatar_user_icon.png" alt="Foto do usuário" class="details-pictures details-profile-picture">
                            </div>
                            <div class="col-md-4">
                                <div class="row">
                                    <div class="col">
                                        <div class="row mb-2">
                                            <div class="col-6 text-white">Nickname:</div>
                                            <div class="col-6 text-white">sjhony-x</div>
                                        </div>
                                        <div class="row mb-2">
                                            <div class="col-6 text-white">Pontuação:</div>
                                            <div class="col-6 text-white">1000</div>
                                        </div>
                                        <div class="row mb-2">
                                            <div class="col-6 text-white">Vitórias:</div>
                                            <div class="col-6 text-white">50</div>
                                        </div>
                                        <div class="row mb-2">
                                            <div class="col-6 text-white">Derrotas:</div>
                                            <div class="col-6 text-white">20</div>
                                        </div>
                                        <div class="row mb-2">
                                            <div class="col-6 text-white">Posição:</div>
                                            <div class="col-6 text-white">5º</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="containers">
            <div class="row header-row-info">
                <div class="col-8 header-info-column">
                    <i class="fas fa-info-circle header-info-icon"></i>
                    <div>
                        <p class="mb-0">Info</p>
                    </div>
                </div>
                <div class="col-2 header-scores-column">
                    <i class="fas fa-chart-bar me-2"></i>
                    <div>
                        <p class="mb-0">Scores</p>
                        <p class="mb-0">500</p>
                    </div>
                </div>
                <div class="col-2 header-players-column">
                    <i class="fas fa-users me-2"></i>
                    <div>
                        <p class="mb-0">Players</p>
                        <p class="mb-0">5</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="containers">
            <div class="container">
                <div class="row row-item-list d-flex align-items-center mb-3">
                    <div class="col-2">
                        <img src="" alt="User Photo" class="list-user-photo" id="user-foto">
                    </div>
                    <div class="col-5">
                        <p class="list-nickname"><strong class="p-3 shadow" id="nickname"></strong></p>
                    </div>
                    <div class="col-3">
                        <p class="list-scores"><strong class="p-3 shadow" id="user-scores"></strong></p>
                    </div>
                    <div class="col-2">
                        <p class="list-user-game-status">
                            <strong class="p-3 shadow" id="user-playing"></strong>
                        </p>
                    </div>
                </div>
            </div>
    </div>
</div>

` 

const start = () => {
    gameInfoService.gameInfo().then(
      res => {
            document.getElementById('nickname').innerHTML = res[0].nickname;
            document.getElementById('user-foto').src = `http://localhost:8003/${res[0].photo}`;
            document.getElementById('user-scores').innerHTML = `Scores: ${res[0].scores}`;
            
            const userPlaying = document.getElementById('user-playing');
            const icon = document.createElement('i');
            icon.classList.add('fa-solid', 'fa-circle', 'me-2', 'mt-2');
            icon.style.color = res[0].playing ? 'green' : 'yellow';
            userPlaying.appendChild(icon);

            const labelPlaying = document.createElement('strong');
            labelPlaying.setAttribute('id', 'user-playing-label');
            labelPlaying.textContent = res[0].playing ? 'In Game' : 'Free';
            userPlaying.appendChild(labelPlaying);
      });
    console.log('GameInfo View');
  }

export default new GameInfoView(html, start);