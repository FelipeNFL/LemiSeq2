import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SlotsViewComponent } from './slots-view.component';

describe('SlotsViewComponent', () => {
  let component: SlotsViewComponent;
  let fixture: ComponentFixture<SlotsViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SlotsViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SlotsViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
