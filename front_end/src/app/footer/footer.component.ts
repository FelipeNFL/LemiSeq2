import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { UserService } from '../services/user.service';
import { Subscription } from 'rxjs/Subscription';
import { ChrompackServiceObservable } from '../services/chrompack-observable.service';

@Component({
  selector: 'footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  refreshMetricsSubscription: Subscription;
  name: string;
  plates = 0;
  samples = 0;
  subjects = 0;

  constructor(private authService: AuthService,
              private userService: UserService,
              private chrompackServiceObservable: ChrompackServiceObservable) { }

  ngOnInit() {

    this.refreshMetricsSubscription = this.chrompackServiceObservable.getRefreshResult().subscribe(() => {
      this.refreshMetrics();
    });

    this.name = this.authService.getFullname();

    this.refreshMetrics();
  }

  refreshMetrics() {
    this.userService.getMetrics().subscribe(data => {
      this.plates = data.chrompacks;
      this.samples = data.samples;
      this.subjects = data.subjects;
    }, err => {
      console.log(err);
    });
  }
}
