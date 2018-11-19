import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { UserService } from '../services/user.service';
import { Subscription } from 'rxjs/Subscription';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';
import { AlertsService } from '../services/alerts.service';

@Component({
  selector: 'footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  refreshMetricsSubscription: Subscription;
  refreshLoginSubscription: Subscription;
  isLogged: boolean;
  name: string;
  plates = 0;
  samples = 0;
  subjects = 0;

  constructor(private authService: AuthService,
              private alerts: AlertsService,
              private userService: UserService,
              private chrompackServiceObservable: ChrompackServiceObservable) { }

  ngOnInit() {

    this.refreshMetricsSubscription = this.chrompackServiceObservable.getRefreshResult().subscribe(() => {
      this.refreshMetrics();
    });

    this.refreshLoginSubscription = this.authService.refreshLogin().subscribe(statusLogin => {
      this.isLogged = statusLogin;
    });

    this.name = this.authService.getFullname();
    this.isLogged = this.authService.isLogged();
    this.refreshMetrics();
  }

  refreshMetrics() {
    this.userService.getMetrics().subscribe(data => {
      this.plates = data.chrompacks;
      this.samples = data.samples;
      this.subjects = data.subjects;
    }, err => {
      this.alerts.error("There are errors to refresh your metrics in footer bar", err);
    });
  }

  logout() {
    this.authService.logout();
  }
}
