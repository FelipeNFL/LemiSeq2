import { Component, OnInit } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { UserService } from '../services/user.service';

@Component({
  selector: 'footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  name: string;
  plates = 0;
  samples = 0;
  subjects = 0;

  constructor(private authService: AuthService, private userService: UserService) { }

  ngOnInit() {
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
